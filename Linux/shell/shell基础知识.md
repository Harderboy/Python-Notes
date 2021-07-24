# shell基础知识

## 为什么使用 `#!/usr/bin/env bash`

```bash
#!/usr/bin/env bash

echo "hello world!"
```

详解：

- 注释符号 #
- 文件起始处的 `#!` 声明自己是一个脚本文件
- 当前shell脚本默认使用的解释器
- 查看当前正在使用shell解释器
  `ps | grep $$`

**为什么使用 `#!/usr/bin/env bash` ？**
当我们通过 `./target.sh` 执行脚本时：

- 避免目标系统上的解释器路径和预期不一致
  - 例如同时存在多个版本的 Bash，通过环境变量设置的优先解释器路径不同于期望的 `/bin/bash`

如果我们通过 `bash target.sh` 或 `/bin/bash target.sh` 执行脚本则上述设置相当于原本的注释行作用

## 编写健壮的 shell 脚本

`set -e`: 脚本只要发生错误，就终止执行
`set +e`: 关闭 `-e` 选项

`set -o pipefail`

- `set -e` 不能终止管道命令中执行出错的语句
  - 只要最后一个子命令不失败，管道命令总是会执行成功
- `set -eo pipefail` 可以让脚本在更严格的条件下执行

## 参考资料

[第四章：shell 脚本编程基础](https://github.com/c4pr1c3/LinuxSysAdmin/blob/master/chap0x04.md)