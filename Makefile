current_dir := ${CURDIR}
build:
	python main.py

test:
	docker run -u `id -u`:`id -g` --name e2e -e SELENIUM_HUB="$(selenium_hub)"  -e CLOUD=$(CLOUD) -e REPORT_LOCATION="/reports" -v "${current_dir}"/reports:/reports --net host networkplanner-e2e-test "$(param)" -n $(threads) --count $(repeat) --reruns $(reruns) --html=/reports/results.html --self-contained-html
