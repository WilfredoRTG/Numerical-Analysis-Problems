.DEFAULT_GOAL := help

# See all the available commands.
.PHONY: help
help: 
	@echo "Commands for use: "
	@echo "-- make 2.1"
	@echo "-- make 2.2"
	@echo "-- make 2.3"
	@echo "-- make 2.4"
	@echo "-- make 2.5"
	@echo "-- make 3.1"

# Run the 2.1 algorithm.
.PHONY: 2.1
2.1:
	@python3 Chapter2/2.1.py

# Run the 2.2 algorithm.
.PHONY: 2.2
2.2:
	@python3 Chapter2/2.2.py

# Run the 2.3 algorithm.
.PHONY: 2.3
2.3:
	@python3 Chapter2/2.3.py

# Run the 2.4 algorithm.
.PHONY: 2.4
2.4:
	@python3 Chapter2/2.4.py

# Run the 2.5 algorithm.
.PHONY: 2.5
2.5:
	@python3 Chapter2/2.5.py

# Run the 3.1 algorithm.
.PHONY: 3.1
3.1:
	@python3 Chapter3/3.1.py

# Run the 3.2 algorithm.
.PHONY: 3.2
3.2:
	@python3 Chapter3/3.2.py

# Run the 3.4 algorithm.
.PHONY: 3.4
3.4:
	@python3 Chapter3/3.4.py

# Run the 3.5 algorithm.
.PHONY: 3.5
3.5:
	@python3 Chapter3/3.5.py