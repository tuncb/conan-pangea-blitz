conan export-pkg . blitz/1.0.1@tuncb/pangea -s os=Windows -s compiler="Visual Studio" -s arch="x86_64" -s compiler.toolset=v141 --force
conan test ./test_package blitz/1.0.1@tuncb/pangea -s build_type=Debug -s os=Windows -s compiler="Visual Studio" -s arch="x86_64" -s compiler.toolset=v141
conan test ./test_package blitz/1.0.1@tuncb/pangea -s build_type=Release -s os=Windows -s compiler="Visual Studio" -s arch="x86_64" -s compiler.toolset=v141
