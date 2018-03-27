#!/usr/bin/env python
#
# Modified by Brian LaShomb (2018)
# Based on 'VersionSplitter', Copyright Elliot Jordan 2015
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from autopkglib import Processor, ProcessorError


__all__ = ["VersionRemix"]


class VersionRemix(Processor):

    """This processor splits version numbers and returns the specified index.
    By default, it splits using a space, and returns the first item.
    Default behavior example: "3.0.8 :074a131:" --> "3.0.8"

    More examples (with "split_on" in parentheses and "index" in brackets):
    - "8.3.1.1 (154179)" --> (" ")[0] -->"8.3.1.1"
    - "1.3.1-stable" --> ("-")[0] -->"1.3.1"
    - "macosx_64bit_3.0" --> ("_")[2] -->"3.0"
    """

    input_variables = {
        "version": {
            "required": True,
            "description": "The version string that needs splitting."
        },
        "find": {
            "required": False,
            "description": "The character(s) to find in the "
                           "version. Used with 'replace'."
        },
        "substitute": {
            "required": False,
            "description": "The character(s) to replace in the "
                           "version. Works with 'find'. "
                           "(Defaults to a decimal point.)"
        }
    }
    output_variables = {
        "version": {
            "description": "The cleaned up version string."
        }
    }
    description = __doc__

    def main(self):
        find = self.env.get("find")
        substitute = self.env.get("substitute", ".")
        # self.env["version"] = self.env["version"].replace(find, substitute)
        self.output("Version: %s" % self.env["version"].replace(find, substitute))


if __name__ == "__main__":
    processor = VersionRemix()
    processor.execute_shell()
