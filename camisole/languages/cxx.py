from camisole.models import Lang


class CXX(Lang, name="C++"):
    source_ext = '.cc'
    compiler = 'g++'
    compile_opts = ['-std=c++14', '-Wall', '-Wextra', '-O2']
    reference_source = r'''
#include <iostream>
int main()
{
    std::cout << 42 << std::endl;
    return 0;
}
'''
