import pandas as pd
from pandas.api.types import is_string_dtype
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

def add_feedback_text_counts(
    hospital_df: pd.DataFrame,
    feedback_col: str = "feedback",
    word_count_col: str = "feedback_word_count",
    char_count_col: str = "feedback_character_count",
) -> pd.DataFrame:
    """
    Add word and character count columns from a feedback text column.

    Character count includes spaces and punctuation.
    """
    if feedback_col not in hospital_df.columns:
        raise ValueError(f"Column '{feedback_col}' not found in DataFrame.")

    feedback_text = hospital_df[feedback_col].fillna("").astype(str)

    hospital_df[word_count_col] = feedback_text.str.split().str.len()
    hospital_df[char_count_col] = feedback_text.str.len()

    return hospital_df


def add_word_count_column(
    df: pd.DataFrame,
    source_col: str,
    output_col: str | None = None,
) -> pd.DataFrame:
    """
    Add a word-count column for any text column in a DataFrame.

    Tokenization is whitespace-based.
    """
    if source_col not in df.columns:
        raise ValueError(f"Column '{source_col}' not found in DataFrame.")

    series = df[source_col]
    non_null_values = series.dropna()

    is_text_column = is_string_dtype(series) or non_null_values.map(lambda v: isinstance(v, str)).all()
    if not is_text_column:
        raise TypeError(f"Column '{source_col}' is not a string/text column.")

    if output_col is None:
        output_col = f"{source_col} Word Count"

    df[output_col] = series.fillna("").astype(str).str.split().str.len()
    return df


def add_staff_mention_column(
    df: pd.DataFrame,
    source_col: str = "feedback",
    staff_output_col: str = "Mentions Staff",
) -> pd.DataFrame:
    """
    Add a numeric boolean column indicating if staff is mentioned.

    Matching is case-insensitive and uses whole words.
    Output values are 0 (not mentioned) or 1 (mentioned).
    """
    if source_col not in df.columns:
        raise ValueError(f"Column '{source_col}' not found in DataFrame.")

    text = df[source_col].fillna("").astype(str)
    df[staff_output_col] = text.str.contains(r"\bstaff\b", case=False, regex=True).astype(int)
    return df


def add_service_mention_column(
    df: pd.DataFrame,
    source_col: str = "feedback",
    service_output_col: str = "Mentions Service",
) -> pd.DataFrame:
    """
    Add a numeric boolean column indicating if service is mentioned.

    Matching is case-insensitive and uses whole words.
    Output values are 0 (not mentioned) or 1 (mentioned).
    """
    if source_col not in df.columns:
        raise ValueError(f"Column '{source_col}' not found in DataFrame.")

    text = df[source_col].fillna("").astype(str)
    df[service_output_col] = text.str.contains(r"\bservice\b", case=False, regex=True).astype(int)
    return df


def add_staff_and_service_mention_columns(
    df: pd.DataFrame,
    source_col: str = "feedback",
    staff_output_col: str = "Mentions Staff",
    service_output_col: str = "Mentions Service",
) -> pd.DataFrame:
    """
    Add both numeric boolean mention columns for staff and service.
    """
    df = add_staff_mention_column(df, source_col=source_col, staff_output_col=staff_output_col)
    df = add_service_mention_column(df, source_col=source_col, service_output_col=service_output_col)
    return df


def make_rating_wordcloud(
    df: pd.DataFrame,
    rating_value,
    text_col: str = "feedback",
    rating_col: str = "ratings",
    extra_stopwords=None,
    figsize=(10, 6),
):
    # Filter to one ratings group
    subset = df[df[rating_col] == rating_value]

    # Combine text
    text = " ".join(subset[text_col].fillna("").astype(str)).strip()
    if not text:
        raise ValueError(f"No text found for {rating_col}={rating_value}")

    # Build word cloud
    stopwords = set(STOPWORDS)
    if extra_stopwords:
        stopwords.update(extra_stopwords)

    wc = WordCloud(
        width=1200,
        height=600,
        background_color="white",
        stopwords=stopwords,
        collocations=False,
    ).generate(text)

    # Plot
    plt.figure(figsize=figsize)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"Word Cloud for {rating_col} = {rating_value}")
    plt.show()

    return wc


from collections import Counter
import re
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS

def plot_top_words_by_rating(
    df,
    rating_value,
    text_col="feedback",
    rating_col="ratings",
    top_n=10,
    extra_stopwords=None,
):
    subset = df[df[rating_col] == rating_value]
    text = " ".join(subset[text_col].fillna("").astype(str)).lower()

    words = re.findall(r"\b[a-z]+\b", text)

    stopwords = set(STOPWORDS)
    if extra_stopwords:
        stopwords.update(extra_stopwords)

    filtered_words = [w for w in words if w not in stopwords]
    counts = Counter(filtered_words).most_common(top_n)

    if not counts:
        print(f"No words found for {rating_col}={rating_value}")
        return

    labels = [w for w, _ in counts]
    values = [c for _, c in counts]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, values)
    plt.title(f"Top {top_n} Words for {rating_col}={rating_value}")
    plt.xlabel("Word")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
