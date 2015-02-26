#!/usr/bin/python
import lutinModule as module
import lutinTools as tools

def get_desc():
	return "speex dsp : Algorithm of speex codec"


def create(target):
	myModule = module.Module(__file__, 'speexdsp', 'LIBRARY')
	# add extra compilation flags :
	#myModule.add_extra_compile_flags()
	# add the file to compile:
	myModule.add_src_file([
		'libspeexdsp/filterbank.c',
		'libspeexdsp/resample.c',
		'libspeexdsp/scal.c',
		'libspeexdsp/fftwrap.c',
		'libspeexdsp/jitter.c',
		'libspeexdsp/mdf.c',
		'libspeexdsp/preprocess.c',
		'libspeexdsp/smallft.c',
		'libspeexdsp/buffer.c',
		'libspeexdsp/kiss_fft.c',
		'libspeexdsp/kiss_fftr.c'
		])
	# name of the dependency
	myModule.add_module_depend('z')
	
	myModule.compile_version_CC(1999)
	
	myModule.add_export_path(tools.get_current_path(__file__) + "/include")
	# configure library :
	
	# Make use of ARM4 assembly optimizations
	#myModule.compile_flags_CC("-DARM4_ASM=1")
	# Make use of ARM5E assembly optimizations
	#myModule.compile_flags_CC("-DARM5E_ASM=1")
	# Make use of Blackfin assembly optimizations
	#myModule.compile_flags_CC("-DBFIN_ASM=1")
	# Disable all parts of the API that are using floats
	#myModule.compile_flags_CC("-DDISABLE_FLOAT_API=1")
	# Enable valgrind extra checks
	#myModule.compile_flags_CC("-DENABLE_VALGRIND=1")
	# Symbol visibility prefix */
	#define EXPORT __attribute__((visibility("default")))
	myModule.compile_flags_CC("-DEXPORT=''")
	# Debug fixed-point implementation */
	#myModule.compile_flags_CC("-DFIXED_DEBUG=1")
	# Compile as fixed-point / floating-point
	if True:
		myModule.compile_flags_CC("-DFIXED_POINT")
	else:
		myModule.compile_flags_CC("-DFLOATING_POINT")
		# Enable NEON support */
		#myModule.compile_flags_CC("-D_USE_NEON=1")
		# Enable SSE support */
		myModule.compile_flags_CC("-D_USE_SSE=1")
		# Enable SSE2 support */
		myModule.compile_flags_CC("-D_USE_SSE2=1")
	# Define to 1 if you have the <alloca.h> header file.
	myModule.compile_flags_CC("-DHAVE_ALLOCA_H=1")
	# Use FFT from OggVorbis */
	myModule.compile_flags_CC("-DUSE_SMALLFT=1")
	# Use C99 variable-size arrays */
	myModule.compile_flags_CC("-DVAR_ARRAYS=1")
	
	return myModule


