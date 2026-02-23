import math
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px

sns.set_palette("flare")

def plot_dists(df, kde_only=False, include_mean=True, include_median=True):
    num_cols = df.select_dtypes(include="number").columns
    n = len(num_cols)

    ncols = math.ceil(math.sqrt(n))
    nrows = math.ceil(n / ncols)

    plt.rcParams.update({"font.size": 8})
    fig, axes = plt.subplots(nrows, ncols, figsize=(4*ncols, 2.6*nrows))
    axes = np.array(axes).ravel()

    for i, col in enumerate(num_cols):
        ax = axes[i]
        if kde_only:
            sns.kdeplot(df[col], ax=ax)
        else:
            sns.histplot(df[col], bins="auto", kde=True, ax=ax)
        
        if include_mean:
            mean_val = df[col].mean()
            ax.axvline(mean_val, linestyle='--', linewidth=1.5, label=f'Mean = {mean_val:.2f}', color="b")

        if include_median:
            median_val = df[col].median()
            ax.axvline(median_val, linestyle='-', linewidth=1.5, label=f'Median = {median_val:.2f}', color="r")

        if include_mean or include_median:
            ax.legend(fontsize=6)
        ax.set_title(col, fontsize=9)
        ax.tick_params(labelsize=7)
        ax.grid(alpha=0.2)

    for j in range(i + 1, len(axes)):
        axes[j].axis("off")

    fig.tight_layout()
    plt.show()

def plot_box_plots(df):
    num_cols = df.select_dtypes(include="number").columns
    n = len(num_cols)

    ncols = math.ceil(math.sqrt(n))
    nrows = math.ceil(n / ncols)

    plt.rcParams.update({"font.size": 8})
    fig, axes = plt.subplots(nrows, ncols, figsize=(4*ncols, 2.6*nrows))
    axes = np.array(axes).ravel()

    for i, col in enumerate(num_cols):
        ax = axes[i]
        sns.boxplot(df[col], ax=ax)
        ax.set_title(col, fontsize=9)
        ax.tick_params(labelsize=7)
        ax.grid(alpha=0.2)

    for j in range(i + 1, len(axes)):
        axes[j].axis("off")

    fig.tight_layout()
    plt.show()

def plot_corr(df, annot=False):
    method="pearson"
    num_df = df.select_dtypes(include="number")
    corr = num_df.corr(method=method)

    plt.figure(figsize=(13,8))
    sns.heatmap(
        corr,
        cmap="coolwarm",
        center=0,
        annot=annot,
        fmt=".2f",
        linewidths=0.5
    )
    
    plt.title(f"Correlation Matrix (Heatmap)", fontsize=14)
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()


def plot_corr_triangle(df,annot=False):
    method="pearson"
    num_df = df.select_dtypes(include="number")
    corr = num_df.corr(method=method)

    mask = np.triu(np.ones_like(corr, dtype=bool))

    plt.figure(figsize=(13, 8))
    sns.heatmap(
        corr,
        mask=mask,
        cmap="coolwarm",
        annot=annot,
        center=0,
        linewidths=0.5
    )

    plt.title(f"Correlation Matrix (Heatmap - Triangle Only)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def plot_corr_plotly(df, method="pearson"):
    num_df = df.select_dtypes(include="number")
    corr = num_df.corr(method=method)

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        zmin=-1, zmax=1,
        aspect="auto" 
    )

    fig.update_layout(
        title=f"{method.capitalize()} Correlation (Interactive)",
        width=1200,
        height=720,
        font=dict(size=10),
        margin=dict(l=20, r=20, t=60, b=20)
    )

    fig.update_xaxes(tickangle=45, tickfont=dict(size=9))
    fig.update_yaxes(tickfont=dict(size=9))

    fig.show()


def plot_scatter_corr(df, sample_size=None):
    num_df = df.select_dtypes(include="number")
    
    # Optional sampling (very recommended)
    if sample_size is not None:
        num_df = num_df.sample(sample_size, random_state=42)

    sns.set_style("whitegrid")

    g = sns.pairplot(
        num_df,
        corner=True,     
        diag_kind="kde",  
        plot_kws={"alpha": 0.4, "s": 15}
    )

    plt.tight_layout()
    plt.show()

def plot_scatter_corr_line(df, sample_size=None):
    num_df = df.select_dtypes(include="number").replace([np.inf, -np.inf], np.nan).dropna()

    if sample_size is not None and len(num_df) > sample_size:
        num_df = num_df.sample(sample_size, random_state=42)

    sns.set_style("whitegrid")

    g = sns.pairplot(
        num_df,
        corner=True,
        diag_kind="kde",
        kind="reg",
        plot_kws={
            "scatter_kws": {"alpha": 0.35, "s": 12},
            "line_kws": {"color": "blue", "linewidth": 2}
        }
    )

    plt.tight_layout()
    plt.show()

def plot_scatter_corr_curved(df, sample_size=1500, jitter=1e-3):
    num_df = df.select_dtypes(include="number").replace([np.inf, -np.inf], np.nan).dropna()

    if sample_size is not None and len(num_df) > sample_size:
        num_df = num_df.sample(sample_size, random_state=42)

    # add small jitter to reduce duplicate-value problems
    num_df = num_df + np.random.normal(0, jitter, size=num_df.shape)

    sns.set_style("whitegrid")

    g = sns.pairplot(
        num_df,
        corner=True,
        diag_kind="kde",
        kind="reg",
        plot_kws={
            "lowess": True,
            "scatter_kws": {"alpha": 0.30, "s": 10},
            "line_kws": {"color": "blue", "linewidth": 2}
        }
    )

    plt.tight_layout()
    plt.show()
