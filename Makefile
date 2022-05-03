vm:
	g++ -o multi_ys_VM test_multi_ys_vM_shear.cpp vonMises_yield_surface.cpp MultiYieldSurfaceMaterial.cpp -std=c++11 -Wall
	python test_MYS_vM.py
	
dp:
	g++ -o multi_ys_DP test_multi_ys_DP_shear.cpp DruckerPrager_yield_surface.cpp MultiYieldSurfaceMaterial.cpp -std=c++11 -Wall
	python test_MYS_DP.py

rmc:
	g++ -o multi_ys_RMC test_multi_ys_RMC_shear.cpp RoundedMohrCoulomb_yield_surface.cpp MultiYieldSurfaceMaterial.cpp -std=c++11 -Wall
	python test_MYS_RMC.py	
	
clean:
	-rm -f  multi_ys
	-rm -f  strain_stress.txt
	-rm -f  results.pdf