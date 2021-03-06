from camisole.models import Lang


class FSharp(Lang, name="F#"):
    source_ext = '.fs'
    compiler = 'fsharpc'
    compile_opts = ['-O']
    version_lines = 4
    interpreter = 'mono'
    reference_source = r'''
#light
open System
let () =
    Printf.printf "42\n"
'''
