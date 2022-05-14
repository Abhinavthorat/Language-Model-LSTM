

class Utils():
    import numpy as np
    import codecs
    import pandas as pd
    
    @staticmethod
    def read_data(filepath,lines):
    
        """
        filepath is address of file
        lines == All will read complete document else specified number of lines
            """
        if lines=='all':
            with codecs.open(filepath,encoding='UTF-8') as f:
                data = f.readlines()
            
        else:
            with codecs.open(filepath,encoding='UTF-8') as f:
                data = f.readlines(lines)
        return data