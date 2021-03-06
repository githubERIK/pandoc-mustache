"""
Pandoc filter to apply mustache templates on regular text.
"""
import yaml
from jinja2 import StrictUndefined, Template
from panflute import Code, CodeBlock, Str, run_filter


def prepare(doc):
    """Parse metadata to obtain list of mustache templates,
    then load those templates.
    """
    doc.mustache_files = doc.get_metadata("mustache")
    if isinstance(
        doc.mustache_files, str
    ):  # process single YAML value stored as string
        if not doc.mustache_files:
            doc.mustache_files = None  # switch empty string back to None
        else:
            doc.mustache_files = [doc.mustache_files]  # put non-empty string in list

    if doc.mustache_files is not None:
        doc.mustache_hashes = [
            yaml.load(open(file, "r").read(), Loader=yaml.SafeLoader)
            for file in doc.mustache_files
        ]
        doc.mhash = {
            k: v for mdict in doc.mustache_hashes for k, v in mdict.items()
        }  # combine list of dicts into a single dict
    else:
        doc.mhash = None


def action(elem, doc):
    """Apply combined mustache template to all strings in document."""
    if type(elem) in (Str, CodeBlock, Code) and doc.mhash is not None:
        template = Template(source=elem.text, undefined=StrictUndefined)
        elem.text = template.render(**doc.mhash)
        return elem


def main(doc=None):
    return run_filter(action, prepare=prepare, doc=doc)


if __name__ == "__main__":
    main()
