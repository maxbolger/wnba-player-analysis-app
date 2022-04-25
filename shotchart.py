import numpy as np
import matplotlib.pyplot as plt

def shot_chart(df_l, df):
    """
    Draws a shot chart for given shots.

            Parameters:
                df_l (pandas.DataFrame): league-wide data to compare to
                df (pandas.DataFrame): Subset data (usually an individual player)

            Returns:
                ax (matplotlib.figure): A matplotlib figure of the shot chart
    """
    shots_hex = plt.hexbin(
        df.loc_x, df.loc_y,
        extent=(-250, 250, 422.5, -47.5), 
        cmap='Blues', gridsize=15
        )
    plt.close()

    makes_df = df[df.shot_made_flag == 1]
    makes_hex = plt.hexbin(
        makes_df['loc_x'], makes_df['loc_y'],
        extent=(-250, 250, 422.5, -47.5),
        cmap=plt.cm.Reds, gridsize=15
        )
    plt.close()

    pcts_by_hex = makes_hex.get_array() / shots_hex.get_array()

    shots_hex_lg = plt.hexbin(
        x=df_l.loc_x, y=df_l.loc_y,
        extent=(-250, 250, 422.5, -47.5),
        cmap='Blues', gridsize=15
        )

    makes_df_lg = df_l[df_l.shot_made_flag == 1]
    makes_hex_lg = plt.hexbin(
        makes_df_lg['loc_x'], makes_df_lg['loc_y'],
        extent=(-250, 250, 422.5, -47.5), cmap=plt.cm.Reds, gridsize=15)
    plt.close()
  
    league_pcts_by_hex = makes_hex_lg.get_array() / shots_hex_lg.get_array()
    league_pcts_by_hex[np.isnan(league_pcts_by_hex)] = 0  # convert NAN values to 0

    shots_by_hex = shots_hex.get_array()

    freq_by_hex = shots_by_hex / sum(shots_by_hex)
    filter_threshold = 0.009

    for i in range(len(freq_by_hex)):
        if freq_by_hex[i] < filter_threshold:
            freq_by_hex[i] = 0
    x = [i[0] for i in shots_hex.get_offsets()]
    y = [i[1] for i in shots_hex.get_offsets()]

    sizes = freq_by_hex
    sizes = sizes / max(sizes) * 500
    max_freq = max(freq_by_hex)
    max_size = max(sizes)

    rel_pcts_by_hex = pcts_by_hex - league_pcts_by_hex
    clip_cmap = (-0.1, 0.1)
    z = np.array([max(min(i, max(clip_cmap)), min(clip_cmap)) for i in rel_pcts_by_hex]) * 100

    fig, ax = plt.subplots(figsize=(5, 4.7))
    ax.set_facecolor(color='#0E1117')
    # fig, ax = plt.subplots()
    plt.xlim(250, -250)
    plt.ylim(-47.5, 422.5)

    if df.shot_made_flag.mean() == 1:
      scatter = plt.scatter(x, y, c='#2f3989', s=sizes, cmap='RdYlBu', marker='h')
    else:
      scatter = plt.scatter(x, y, c=z, s=sizes, cmap='RdYlBu', marker='h')

    cur_axes = plt.gca()
    cur_axes.axes.get_xaxis().set_visible(False)
    cur_axes.axes.get_yaxis().set_visible(False)

    # legend1 = plt.legend(
    #     *scatter.legend_elements(num=5, fmt="{x:.0f}%"),
    #     loc="upper right",
    #     title='Shot acc',
    #     title_fontsize=6,
    #     fontsize=4,
    #     markerscale=1,
    #     ncol=5,
    #     frameon=False,
    #     labelcolor='white'
    #     )
    # plt.setp(legend1.get_title(), color='white')
    # legend2 = plt.legend(
    #     *scatter.legend_elements(
    #         'sizes',num=6,alpha=0.8,
    #         fmt="{x:.1f}%", func=lambda s: s / max_size * max_freq * 100
    #     ),
    #     loc='upper left',
    #     title='Freq (%)',
    #     )
    # plt.gca().add_artist(legend1)

    plt.text(
        x=-142, y=391,
        s="Field Goal Percentage\nCompared to League Average",
        color="#fafafa", size=6.5, ha='center'
        )
    plt.text(x=-52, y=351, s="Below\nAverage", color="#fafafa", size=5.5)
    plt.scatter(x=-95, y=370, s=300, marker='h', c="#981d2b")
    plt.scatter(x=-119, y=370, s=300, marker='h', c="#eb945e")
    plt.scatter(x=-143, y=370, s=300, marker='h', c="#fffec7")
    plt.scatter(x=-167, y=370, s=300, marker='h', c="#98c1d9")
    plt.scatter(x=-192, y=370, s=300, marker='h', c="#2f378e")
    plt.text(x=-236, y=351, s="Above\nAverage", color="#fafafa", size=5.5, ha='right')

    plt.scatter(x=194, y=377, s=300, marker='h', c="#fafafa")
    plt.scatter(x=206, y=356, s=150, marker='h', c="#fafafa")
    plt.text(x=226, y=403, s="Shot Frequency", color="#fafafa", size=6.5)
    plt.text(x=195, y=352, s="Low", color="#fafafa", size=5.75)
    plt.text(x=180, y=374, s="High", color="#fafafa", size=5.75)

    return fig
