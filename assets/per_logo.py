import scanpy as sc
from lets_plot import *

import cellestial as cl

data = sc.read("../data/pbmc3k_pped.h5ad")


plot = cl.umap(data, axis_type=None, size=0.12)
plot = plot + theme_void() + ggsize(200, 200)
plot = plot + theme(legend_position="none")
plot = plot + theme(
    legend_background=element_blank(),
    plot_background=element_blank(),
) + scale_color_hue()

plot.to_pdf("test/per_logo.pdf")