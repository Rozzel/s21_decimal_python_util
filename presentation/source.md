# s21_decimal-2

- Comparison
	- is_less
	- is_less_or_equal
	- is_greater
	- is_greater_or_equal

```c
int compare(s21_decimal left, s21_decimal right);
```

---

## Team

- **Valeriia** <sup>Rickonsh</sup>

- **Nikita** <sup>Chauspot</sup>

- **Anton** <sup>Bettiema</sup>

- **Vladislav** <sup>Lothostr</sup>

---

## Valgrind

Checking for memory leaks

```bash
==23432== HEAP SUMMARY:
==23432== in use at exit: 0 bytes in 0 blocks
==23432== total heap usage:
			12,609 allocs,
			12,609 frees,
			9,506,722 bytes allocated
==23432== All heap blocks were freed
			-- no leaks are possible
==23432== For lists of detected
			and suppressed errors,
			rerun with: -s
==23432== ERROR SUMMARY: 0 errors from 0 contexts
			(suppressed: 0 from 0)
```


---

## Makefile

- CC=gcc
- -std=c11
- make
	- **OS**: fedora, ubuntu, alpine, darwin
		- all
		- clean
		- test
		- s21.decimal.a
		- gcov_report
- Modular makefile

---

## Style

- makefiles
	- style.mk
		- test-style_ci

---

## Debugging

- Configuring debagging in the project

---

## Docker

- Dockerfile
	- .alpine
	- .ubuntu
- CI/CD
	- alpine

---

## CI/CD

- .gitlab-ci.yml

---

## Organization of work

- Notion
- Git graph
- live Share

---

## Doxygen

- Doxyfile
- File_lists
	- 21_decimal.h
	- All files

---