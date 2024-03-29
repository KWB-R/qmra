Welcome to QMRA's documentation!
================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


QMRA is a Django project which experiments with deploying state-of-the-art techniques 
for Quantitative Microbial Risk Assessment (QMRA). 

The implemented simulations rely on a freely available `database <https://kwb-r.github.io/qmra.db/>`_, which was developed within the research project `Aquanes <https://cordis.europa.eu/project/id/689450>`_.

The tool allows to estimate the risk of infection for three reference pathogen (Rotavirus, *Campylobacer jejuni*, and *Cryptosporidium parvum*) for mutliple source waters and treatment scenarios.

Basic functionality
===================

The tool provides the user with a graphical user interface, which allows the configuration of the most important model input variables
for a Quantitative Microbial Risk Assessment (QMRA) in the field of water supply and water reuse systems. 
Based on the user's configuration, the tool runs a Monte Carlo Simulation (MCS) to simulate the range of potential risk outcomes.

The model inputs, which can be configured by the user inlcude:

#. the source water quality
#. the implemented water treatment
#. the exposure based on the intended use (drinking, irrigation etc.)

The simulated risk is expressed and visualized both in term of annual risk of infection and disability adjusted life years (DALYs).

Default values vs. user inputs
===============================

QMRA allows the user to perform a first-stage risk assessment of the water supply system by two different options. 
First, by using default values derived from international guideline documents and scientific literature (see `database <https://kwb-r.github.io/qmra.db/>`_). 
Second, by creating own scenarios (treatments, exposure scenarios) and providing numeric values for the model input of interest. 
The ability to create own scenarios based on self-created treatments and exposure scenarios is a powerfull feature, which enables users to
adapt the tool the specific local needs. Examples to use this feature to answer specific questions include:

#.  comparison of risks caused by specific activities at the wastewateer treatment plants.
#.  derivation of necessary log-removal values by creating unspecified treatments representing specific LRVs.
#.  comparison of different system configurations by creating treatments with specific configurations (e.g. low / high UV dose disinfection)   


User specific treatments
########################

Users are able to create own treatments. For this, the user has to provide a name, and short description of the treatment as well as
numerical values for the treatment performances in terms of log removal values (LRV). 

LRVs have to be provided for each group of pathogen (bacteria, viruses, protozoa). The input form for LRV shows input fields for the
minimum (min) and maximum (max) LRV. The range defined by these value represents the uncertainty about the **average** (i.e. mean) logremoval.

LRV values are determined by measuring pathogens (or indicator organisms) in the influent and effluent of the treatment step and calculating LRV by:

\

\

.. math::

    LRV = log_{10} \frac{Influent\:concentration}{Effluent\:concentration}

\

\

.. note::

    For calculating the overall mean performance of the system, the mean of the 
    *removal fractions* has to be calculated and not the mean of the log-values. 
    So, if your individual LRV observations are 1, 2, and 3, the mean LRV is **not** 2, 
    but only 1.43. 

\

User specific exposure scenarios
################################

Users are able to create own exposure scenarios. Exposure scenrarios are represented by point estimates for the number of exposure events per year,
and the ingested water volume ingested per event. As for user specific treatments the user can specify a name and short description 
for each exposure scenario.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
