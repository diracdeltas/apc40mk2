all :
	python -m compileall *.py
dist :
	python -m compileall *.py && mkdir apc40mkii_azuki && cp *.pyc apc40mkii_azuki/ && zip -r release.zip apc40mkii_azuki && rm -r apc40mkii_azuki
