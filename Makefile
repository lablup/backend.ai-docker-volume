PLUGIN_PATH = ./plugin
PLUGIN_NAME = lablup/backend.ai-docker-volume

all: clean rootfs create

clean:
	@echo "Purge plugin directory ${PLUGIN_PATH}"
	@rm -rf ${PLUGIN_PATH}

rootfs:
	@echo "Build rootfs image"
	@docker build -t rootfsimage .
	@docker create --name rootfs rootfsimage
	@echo "Create rootfs directory in ${PLUGIN_PATH}/rootfs"
	@mkdir -p ${PLUGIN_PATH}/rootfs
	@docker export rootfs | tar -x -C ${PLUGIN_PATH}/rootfs || true
	@docker rm -vf rootfs
	@docker rmi rootfsimage
	@echo "Copy config.json to ${PLUGIN_PATH}"
	@cp config.json ${PLUGIN_PATH}

create:
	@docker plugin rm -f ${PLUGIN_NAME} || true
	@echo "Create new docker plugin ${PLUGIN_NAME} from ${PLUGIN_PATH}"
	@docker plugin create ${PLUGIN_NAME} ${PLUGIN_PATH}

enable:
	@echo "Enable docker plugin ${PLUGIN_NAME}"
	@docker plugin enable ${PLUGIN_NAME}
