#!/usr/env/python
import json
from jsoncomment import JsonComment


def main():
    prefix = "xcodebuild/DebugX64/dart"
    postfix = "> ../my_demo/flow_graph.log 2>&1"
    input_json = '''[
                "--no-background-compilation",
                "--optimization-counter-threshold=1",
                // "--print_classes",
                "--print-flow-graph",
                "--print-flow-graph-optimized",
                "--disassemble-optimized",
                "--disassemble",
                // "--trace_compiler",
                // "--trace_optimizing_compiler",
                // "--trace_compilation_trace",
                // "--trace_osr",
                "--trace_inlining",
                // "--trace_range_analysis",
                // "--trace_ssa_allocator",
                // "--trace_type_propagation",
                "--inlining_callee_size_threshold=1",
                "--inlining_caller_size_threshold=1",
                "--print-flow-graph-filter=main.dart",
                "${workspaceFolder}/../my_demo/main.dart",
            ]'''
    parser = JsonComment(json)
    json_array = parser.loads(input_json)
    # print(json_array)
    json_array[:] = map(lambda x: x.replace("${workspaceFolder}/", ""), json_array)
    json_array.insert(0, prefix)
    json_array.append(postfix)
    print("cmdline:")
    print(" ".join(json_array))


if __name__ == '__main__':
    main()
