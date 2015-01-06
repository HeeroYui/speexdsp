#!/usr/bin/python
import lutinModule as module
import lutinTools as tools

def get_desc():
	return "speex dsp (test): echo test algorithm"


def create(target):
	myModule = module.Module(__file__, 'speextestecho', 'BINARY')
	# add extra compilation flags :
	myModule.add_extra_compile_flags()
	# add the file to compile:
	myModule.add_src_file([
		'libspeexdsp/testecho.c'
		])
	
	# name of the dependency
	myModule.add_module_depend('speexdsp')
	
	# add the currrent module at the 
	return myModule


