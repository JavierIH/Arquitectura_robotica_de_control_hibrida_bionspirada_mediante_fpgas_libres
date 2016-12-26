# -*- coding: utf-8 -*-

'''

Python says

A program that generates Verilog code and verify, build and load the code using APIO

Made by Julián Caro Linares

CC-BY-SA

'''

#Libraries
import os
import subprocess

import apio

from apio.managers.scons import SCons
from apio.managers.project import Project

#Variables
path="." #By the time the path it must be the root of the project. Apio needs that (Scons().verify doesn't have a path parameter)
fpgaboard="icezum"
pythonsays_memo="[PYTHON SAYS]: " #Keyword that defines the outputs generated by pythonsays


#APIO CALLING FUNCTIONS

class FPGA_engine(object):

    def __init__(self):
        self.board="icezum"
        self.scons_engine=SCons()
        self.project=Project()


    def config_fpga(self):
        print("\n\n"+pythonsays_memo+"Calling APIO FPGA Board Setup (PROJECT)"+"\n\n")

        #project=Project()
        self.project.create_ini(self.board, path, False)

        #apio.managers.scons.Project.create_ini(fpgaboard_name, path, False) #Another lower level option
        return True

    def verify_hdl(self):
        #subprocess.call('echo "\n\nCalling APIO Verify (SCONS)"' ,shell=True)
        print("\n\n"+pythonsays_memo+"Calling APIO Verify (SCONS)"+"\n\n")

        #scons_engine=SCons()

        self.scons_engine.verify()
        return True

    def build_hdl(self):
        print("\n\n"+pythonsays_memo+"BUILDING CIRCUIT"+"\n\n")

        #Apio building calling (SCONS)

        #scons_engine=SCons()
        '''
        scons_engine.__init__()#Not needed
        scons_engine.build({
            'board': board,
            'fpga': fpga,
            'size': size,
            'type': type,
            'pack': pack
        })
        '''


        self.scons_engine.build({ #Details extracted from boards.json and fpgas.json Device argument must be 0
            'board': "icezum",
            'fpga': "iCE40-HX1K-TQ144",
            'size': "1k",
            'type': "hx",
            'pack': "tq144"
        })

        return True

    def upload_hdl(self):
        print("\n\n"+pythonsays_memo+"UPLOADING CIRCUIT"+"\n\n")

        #scons_engine=SCons()

        self.scons_engine.upload({ #Details extracted from boards.json and fpgas.json Device argument must be 0
            'board': "icezum",
            'fpga': "iCE40-HX1K-TQ144",
            'size': "1k",
            'type': "hx",
            'pack': "tq144"
        }, 0)
        return True

#Main execution
def main():

    fpga=FPGA_engine()
    fpga.config_fpga()
    fpga.verify_hdl()
    fpga.build_hdl()
    fpga.build_hdl()
    fpga.upload_hdl()

    '''
    if config_fpga(fpgaboard)==True:
        print("\n\n"+pythonsays_memo+"FPGA configuration completed")

    if verify_hdl()==True:
        print("\n\n"+pythonsays_memo+"Verification completed, no errors in the code")

    if build_hdl()==True:
        print("\n\n"+pythonsays_memo+"CIRCUIT BUILDED")

    if upload_hdl()==True:
        print("\n\n"+pythonsays_memo+"CIRCUIT UPLOADED")
    '''

if __name__ == "__main__":
 main()
