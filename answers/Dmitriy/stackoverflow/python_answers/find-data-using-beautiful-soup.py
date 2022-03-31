# https://stackoverflow.com/a/71689142/15164646 

from parsel import Selector

html = """
<div class="chartAreaContainer spm-bar-chart">
    <div class="grid custom_popover" data-content="&lt;b&gt;Advertising&lt;/b&gt;" data-html="true" data-original-title="" data-placement="top" data-toggle="popover" data-trigger="hover" role="button" style="width: 40%" title="">40%</div>
    <div class="grid custom_popover" data-content="&lt;b&gt;Media Planning &amp; Buying&lt;/b&gt;" data-html="true" data-original-title="" data-placement="top" data-toggle="popover" data-trigger="hover" role="button" style="width: 35%" title="">35%</div>
    <div class="grid custom_popover" data-content="&lt;b&gt;Branding&lt;/b&gt;" data-html="true" data-original-title="" data-placement="top" data-toggle="popover" data-trigger="hover" role="button" style="width: 20%" title="">20%</div>
    <div class="grid custom_popover" data-content="&lt;b&gt;Event Marketing &amp; Planning&lt;/b&gt;" data-html="true" data-original-title="" data-placement="top" data-toggle="popover" data-trigger="hover" role="button" style="width: 5%" title="">5%</div>
</div>
"""

selector = Selector(text=html)

# regular for loop
for result in selector.css(".grid.custom_popover::text"):
    print(result.get())
    
# or list comprehension
list_result = "\n".join([result.get() for result in selector.css(".grid.custom_popover::text")])
print(list_result)