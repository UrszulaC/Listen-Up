import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


def feature_plot(features):
    # list of music features
    tags = list(features)[:]
    # mean() - is the sum of data divided by the number of data-points
    # tolist() - convert a series to list data type
    info = features.mean().tolist()

    # angles of the visualizer plot
    angles = np.linspace(0, 2 * np.pi, len(tags), endpoint=False)

    # close the visualizer scheme
    info = np.concatenate((info, [info[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    # Size of the visualizer scheme
    fig = plt.figure(figsize=(18, 18))

    ax = fig.add_subplot(221, polar=True)
    ax.plot(angles, info, 'o-', linewidth=2, label="Features", color='gray')
    ax.fill(angles, info, alpha=0.25, facecolor='gray')
    ax.set_thetagrids(angles[0:7] * 180 / np.pi, tags, fontsize=13)

    # position of the number labels
    ax.set_rlabel_position(250)
    # name colour size of the numbers
    plt.yticks([0.2, 0.4, 0.6, 0.8], ["0.2", '0.4', "0.6", "0.8"], color="grey", size=12)
    # space between the circles in the visualizer plot
    # (x,y) x-outside the plot barrier, y - inside the plot space
    plt.ylim(0, 1)

    # location of the legend box
    plt.legend(loc='best', bbox_to_anchor=(0.1, 0.1))

    st.pyplot(plt)