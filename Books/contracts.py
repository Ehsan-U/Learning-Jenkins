from scrapy.contracts import Contract
from scrapy.exceptions import ContractFail


class ValidatorContract(Contract):
    """
    Demo contract which checks the presence of a custom header
    @valid title price rating img
    """

    name = "valid"

    def post_process(self, output):
        for item in output:
            if 'http' not in item.get("img",''):
                raise ContractFail(f"Invalid img url: {item.get('img')}")
        return output