from conans import ConanFile

class BlitzConan(ConanFile):
    name = "blitz"
    version = "1.0.1"
    license = "https://www.apache.org/licenses/LICENSE-2.0"
    url = "https://github.com/tuncb/conan-pangea-blitz"
    description = ("Blitz++ is a C++ template class library"
                   "that provides array objects for scientific computing.\n"
                   "https://github.com/blitzpp/blitz")
    
    settings = "os", "compiler", "build_type", "arch"

    def package_id(self):
        #one package for both Debug and Release 
        self.info.settings.build_type = "Any"
        #one package for both MD and MDd
        self.info.settings.compiler.runtime = "Any"

    def areWeUsingVS2017x64(self):
        return self.settings.os == "Windows" and \
               self.settings.compiler == "Visual Studio" and \
               self.settings.arch == "x86_64" and \
               self.settings.compiler.toolset == "v141"

    def source(self):
        return

    def config(self):
        return

    def build(self):
        return

    def package(self):
        if not self.areWeUsingVS2017x64():
            raise Exception("Binary does not exist for these settings")

        self.copy("*", dst="blitz", src="./include/blitz")
        self.copy("lib/vs2017/x64/blitz*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ['.']
        self.cpp_info.debug.libs = ["blitz_d"]
        self.cpp_info.release.libs = ["blitz"]
