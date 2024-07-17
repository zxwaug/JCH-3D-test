The code was used for the experiments in the article "Bridging the Past and Present: AI-Driven 3D Restoration of Degraded Artefacts for Museum Digital Display", submitted for evaluation to the Journal of Cultural Heritage.
The data set used is uploaded to https://doi.org/10.6084/m9.figshare.24637428.v1

An overview of the project can be seen here: https://www.youtube.com/watch?v=1Slr6eynDvk

The steps of the project are the following:
1. Images of the degraded objects are captured. In the current project, the ones from here ( https://doi.org/10.6084/m9.figshare.24637428.v1 ) are used.
2. Masks are made for these for outlining the parts that are missing. The code for this part is in "Create mask using mouse.ipynb". The masks are also available at the data set from the figshare link above.
3. LaMa can be used to make completions. The implemantation from here ( https://github.com/advimman/lama ) was used in the current project.
4. Diffusion models can be also used. We used the implementation from "Experiments diffusion.ipynb".
5. Analysis of the obtained results can be made. The code from "Check inpainting quality" may be used to replicate the results.
6. Neural Radiance Fields (NERF) implementation is then used to create the 3D model. The implementation is available here: https://www.matthewtancik.com/nerf
7. CloudCompare may be used for evaluating the outputs from NERF.
