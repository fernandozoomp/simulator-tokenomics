
import brownie

BROWNIE_PROJECTUniV3 = brownie.project.load("./v3_core/", name="UniV3ProjectBZR")
print(BROWNIE_PROJECTUniV3)

if brownie.network.show_active() != "development":
    brownie.network.connect("development")

GOD_ACCOUNT = brownie.network.accounts[1]


