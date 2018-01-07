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

    def areWeUsingVS2017x64(self):
        return self.settings.os == "Windows" and \
               self.settings.compiler == "Visual Studio" and \
               self.settings.arch == "x86_64" and \
               self.settings.compiler.toolset == "v141"

    def source(self):
        return

    def config(self):
        self.options.remove("shared")

    def build(self):
        return

    def package(self):
        self.copy("*", dst="blitz", src="./include/blitz")

        if self.areWeUsingVS2017x64():
            self.copy("lib/vs2017/x64/blitz*.lib", dst="lib", keep_path=False)
        else:
            raise Exception("Binary does not exist for these settings")
        
    def package_info(self):
        self.cpp_info.includedirs = ['.']

        if self.settings.build_type == "Debug":
            self.cpp_info.libs = ["blitz_d"]
        elif self.settings.build_type == "Release":
            self.cpp_info.libs = ["blitz"]
        else: 
            raise Exception("Binary does not exist for these settings")
