import pandas as pd
import json
import ast

class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)

        # ✅ FIX 1: Convert tags from string → list
        self.df['tags'] = self.df['tags'].apply(
            lambda x: ast.literal_eval(x) if isinstance(x, str) else x
        )

        # ✅ Add length column
        self.df['length'] = self.df['line_count'].apply(self.categorize_length)

        # ✅ FIX 2: Properly flatten all tags
        all_tags = self.df['tags'].explode().dropna().unique().tolist()
        self.unique_tags = sorted(all_tags)

    def get_names(self):
        return sorted(self.df['name'].dropna().unique().tolist())

    def get_filtered_posts(self, length, language, tag, name=None):
        df_filtered = self.df[
            (self.df['tags'].apply(lambda tags: tag in tags)) &
            (self.df['language'] == language) &
            (self.df['length'] == length)
        ]

        # ✅ FIX 3: Apply name filter only if provided
        if name:
            df_filtered = df_filtered[df_filtered['name'] == name]

        return df_filtered.to_dict(orient='records')

    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5 <= line_count <= 10:
            return "Medium"
        else:
            return "Long"

    def get_tags(self):
        return self.unique_tags

    def get_tags_by_name(self, name):
        if name is None:
            return self.get_tags()

        df_filtered = self.df[self.df['name'] == name]

        if df_filtered.empty:
            return []

        tags = df_filtered['tags'].explode().dropna().unique().tolist()

        return sorted(tags)


if __name__ == "__main__":
    fs = FewShotPosts()

    # 🔍 Debug check
    print(type(fs.df['tags'].iloc[0]))  # should be list

    posts = fs.get_filtered_posts("Short", "English", "Self Care", "Kabir Verma")
    print(posts)