def voting_system():
    print("Simple Voting System")
    print("--------------------")
    
    # Initialize candidates
    candidates = {
        "1": {"name": "Victor", "votes": 0},
        "2": {"name": "Patrick", "votes": 0},
        "3": {"name": "Kamanda", "votes": 0}
    }
    
    # Display candidates
    print("\nCandidates:")
    for key, candidate in candidates.items():
        print(f"{key}. {candidate['name']}")
    
    # Get number of voters
    try:
        num_voters = int(input("\nEnter number of voters: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Voting process
    for i in range(num_voters):
        print(f"\nVoter {i+1}:")
        choice = input("Enter your choice (1-3): ")
        
        if choice in candidates:
            candidates[choice]["votes"] += 1
            print("Vote recorded!")
        else:
            print("Invalid choice. Vote not counted.")
    
    # Display results
    print("\nVoting Results:")
    print("---------------")
    for candidate in candidates.values():
        print(f"{candidate['name']}: {candidate['votes']} votes")
    
    # Find winner
    winner = max(candidates.values(), key=lambda x: x["votes"])
    print(f"\nWinner: {winner['name']} with {winner['votes']} votes!")

# Run the voting system
voting_system()
