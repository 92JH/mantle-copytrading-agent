// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ReputationLog {
    struct AgentRecord {
        uint256 agentId;
        string agentName;
        int256 score;
        string action;
        string reason;
        uint256 timestamp;
    }

    AgentRecord[] public records;
    address public owner;

    event RecordAdded(
        uint256 agentId,
        string agentName,
        int256 score,
        string action,
        uint256 timestamp
    );

    constructor() {
        owner = msg.sender;
    }

    function addRecord(
        uint256 _agentId,
        string memory _agentName,
        int256 _score,
        string memory _action,
        string memory _reason
    ) public {
        records.push(AgentRecord({
            agentId: _agentId,
            agentName: _agentName,
            score: _score,
            action: _action,
            reason: _reason,
            timestamp: block.timestamp
        }));

        emit RecordAdded(_agentId, _agentName, _score, _action, block.timestamp);
    }

    function getRecordCount() public view returns (uint256) {
        return records.length;
    }
}