#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "speex dsp (test): denoise test algorithm"


def create(target):
	myModule = module.Module(__file__, 'speextestdenoise', 'BINARY')
	# add extra compilation flags :
	myModule.add_extra_compile_flags()
	# add the file to compile:
	myModule.add_src_file([
		'libspeexdsp/testdenoise.c'
		])
	
	# name of the dependency
	myModule.add_module_depend('speexdsp')
	
	# add the currrent module at the 
	return myModule


