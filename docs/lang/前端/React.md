## react-router
React Router 是 React 应用程序中用于处理路由的一种库，其可以帮助轻松地构建动态的单页应用程序（SPA）。React Router 充当响应浏览器 URL 的中央协调器，以确保应用程序的状态与 URL 同步。

React Router 提供了三种主要类型的组件：
1.  `<Router>`：这是 React Router 包装器组件中最顶层的类型。它提供了一个祖先上下文，其中包含了路由器所需的所有信息。
2.  `<Route>`：这是代表应用程序中的某个路由的组件。每个 `<Route>` 都包含一个 `path` 属性和一个可以渲染的 `component` 属性。
3.  `<Link>`：这是一种用于链接到不同页面或路由的组件。当链接被点击后，React Router 会确保 URL 改变，并更新匹配的 `<Route>`。

React Router 还提供了一些其他类型的组件，例如 `<Switch>`、`<Redirect>`，以及用于导航和参数传递的 Hooks 和组件。

使用 React Router 可以让我们轻松地构建具有多个页面、嵌套路由和动态 URL 参数的单页面应用程序。