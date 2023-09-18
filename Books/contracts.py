from scrapy.contracts import Contract
from scrapy.exceptions import ContractFail
from scrapy import Request


class ValidatorContract(Contract):
    """
    Contract to validate the output of the Books spider
    @valid title price rating img
    """

    name = "valid"

    def post_process(self, output):
        for item in output:
            if not isinstance(item, Request):
                if 'http' not in item.get("img",''):
                    raise ContractFail(f"Invalid img url: {item.get('img')}")
        return output