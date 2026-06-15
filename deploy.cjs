const { ethers } = require("ethers");
const solc = require("solc");
const fs = require("fs");
require("dotenv").config();

const source = fs.readFileSync("contracts/ReputationLog.sol", "utf8");

const input = {
  language: "Solidity",
  sources: { "ReputationLog.sol": { content: source } },
  settings: { outputSelection: { "*": { "*": ["abi", "evm.bytecode"] } } },
};

const output = JSON.parse(solc.compile(JSON.stringify(input)));
const contract = output.contracts["ReputationLog.sol"]["ReputationLog"];
const abi = contract.abi;
const bytecode = contract.evm.bytecode.object;

async function main() {
  const provider = new ethers.JsonRpcProvider("https://rpc.sepolia.mantle.xyz");
  const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);

  console.log("배포 지갑:", wallet.address);
  console.log("컨트랙트 배포 중...");

  const factory = new ethers.ContractFactory(abi, bytecode, wallet);
  const deployed = await factory.deploy();
  await deployed.waitForDeployment();

  const address = await deployed.getAddress();
  console.log("✅ 컨트랙트 배포 완료!");
  console.log("📌 컨트랙트 주소:", address);
  console.log("🔍 Explorer:", "https://explorer.sepolia.mantle.xyz/address/" + address);
}

main().catch(console.error);