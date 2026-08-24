.PHONY: validate test benchmark check

validate:
	./scripts/validate.sh

test:
	./scripts/test.sh

benchmark:
	./scripts/benchmark.sh

check: validate test
	./scripts/benchmark.sh --check
