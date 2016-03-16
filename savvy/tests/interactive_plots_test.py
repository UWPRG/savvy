import unittest
import os
try:
    import cPickle as pickle
except:
    import pickle


path = os.getcwd()

# Load a sample file to use for testing
comps = pickle.load(open(path + '\\sample_data_files\\unittest_comparisons.pkl', 'rb'))


import data_processing as dp
from collections import OrderedDict
import numpy as np
import pandas as pd

import os
import sys
import interactive_plots as ip
import unittest
from nose.tools import assert_equal, assert_in
import matplotlib
from matplotlib.testing.decorators import image_comparison
from plotting import make_plot, make_second_order_heatmap
from bokeh.plotting import figure, show, output_notebook, output_file

import warnings; warnings.filterwarnings('ignore')

output_notebook()

sa_dict = comps[0]

p = ip.interact_with_plot_all_outputs(sa_dict, demo = True, manual=False) 

class TestInteractWithPlots(unittest.TestCase):

    def test_interact_with_plot_all_outputs_all_widgets_appear(self):
        """
        Are all widgets appearing and are they in right order?
        """
        l = p.widget.children
        self.assertEqual(len(l), 6)
        array_of_widget_names = []
        for i in range(len(l)):
            widgets = p.widget.children[i]
            array_of_widget_names.append(str(widgets.class_own_traits.im_self)
                                         .split('.')[-1].strip('\'>'))
        self.assertEqual(array_of_widget_names, ['BoundedFloatText',
                                       'IntText',
                                       'Checkbox',
                                       'Checkbox',
                                       'Checkbox',
                                       'SelectMultiple'])


    def test_interact_with_plot_all_outputs_default_values(self):
        """
        Are interactive widgets working properly and have proper 
        default values??

        """
        self.assertEqual(p.widget.children[0].value, 0.01)
        self.assertEqual(p.widget.children[1].value, 20.0)
        self.assertEqual(p.widget.children[2].value, True)
        self.assertEqual(p.widget.children[3].value, True)
        self.assertEqual(p.widget.children[4].value, True)
        self.assertEqual(p.widget.children[5].value, ('Tmax', 'Carbon', 'Hydrogen'))


    def test_plot_all_outputs_gives_all_outputs(self):
        """
        Are tabs showing up?
        """
        # this test is in process 


if __name__ == '__main__':
    unittest.main()