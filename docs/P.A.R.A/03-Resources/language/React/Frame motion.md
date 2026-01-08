[根据我搜索到的结果，Framer Motion中有以下几种动画](https://www.framer.com/motion/)[1](https://www.framer.com/motion/)：

-   **简单动画**：使用motion组件和animate属性来执行最常见的动画，例如：`<motion.div animate={{ x: 100 }} />`。
-   **手势动画**：使用一些快捷方式来在手势开始时（如hover, tap, drag, focus和inView）执行一组预设的动画，例如：`<motion.div whileHover={{ scale: 1.2 }} />`。
-   **变体动画**：使用variants属性来定义一组动画状态，并在motion组件之间共享和协调动画，例如：`<motion.div variants={variants} initial="hidden" animate="visible" />`。
-   **手动控制动画**：使用useAnimation自定义钩子来在事件触发时或使用Promise链式调用时控制动画的开始和结束，例如：`const controls = useAnimation(); controls.start({ x: 100 });`。
-   **单值动画**：使用useMotionValue和useTransform自定义钩子来创建和操作单个动画值，例如：`const x = useMotionValue(0); const opacity = useTransform(x, [-200, 0, 200], [0, 1, 0]);`。
-   **内容动画**：使用AnimatePresence和exit属性来在组件卸载时执行出场动画，例如：`<AnimatePresence> {isVisible && <motion.div exit={{ opacity: 0 }} />} </AnimatePresence>`。
-   **硬件加速动画**：使用transformTemplate属性来优化动画性能，例如：`<motion.div style={{ x }} transformTemplate={(x) =>` translate3d(${x}px, 0, 0)`} />`。

[Framer Motion中的动画可以使用不同的过渡类型来定义动画的效果和速度，例如：duration-based tween curves（基于持续时间的补间曲线），spring animations（弹簧动画）和inertia animations（惯性动画）](https://www.framer.com/motion/)[2](https://www.framer.com/motion/transition/)。你可以使用transition属性来指定过渡类型和相关的参数，例如：`<motion.div animate={{ x: 100 }} transition={{ type: "spring", stiffness: 300 }} />`。你也可以为每个动画值指定不同的过渡设置，例如：`<motion.div animate={{ x: 100, opacity: 1 }} transition={{ x: { type: "spring" }, opacity: { duration: 1 } }} />`。