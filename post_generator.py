from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


def generate_post(length, language, tag,name=None, use_emojis=True):
    prompt = get_prompt(length, language, tag,name, use_emojis)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(length, language, tag,name=None, use_emojis=True):
    length_str = get_length_str(length)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    4) Writing Style: {name if name else "General"}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    '''
    if use_emojis:
        prompt += "5) Include relevant emojis where appropriate.\n"
    else:
        prompt += "5) Do NOT use any emojis.\n"
    # prompt = prompt.format(post_topic=tag, post_length=length_str, post_language=language)

    examples = few_shot.get_filtered_posts(length, language, tag, name)

    examples = sorted(examples, key=lambda x: x['engagement'], reverse=True)

    if len(examples) > 0:
        prompt += "\nUse the writing style, tone, and structure similar to the following examples:\n"

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1: # Use max two samples
            break

    return prompt


if __name__ == "__main__":
    print(generate_post("Short", "English", "Money Management","Neha Iyer"))