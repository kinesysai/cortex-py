import trycortex.callables.base as base
import blocks.INPUT.input as input
import blocks.OUTPUT.output as output
"""A templated cortex callable!

Cortex docs:
    https://docs.trycortex.ai

Cortex callable example:
    https://github.com/kinesysai/cortex-py/template.py
"""


callable = base.Callable([
    input.block,
    output.block,
])
