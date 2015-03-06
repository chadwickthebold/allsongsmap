// Application namespace
var asm = asm || {};

(function() {
	'use strict';

	asm.Header = React.createClass({
		render : function() {

			return (
				<header id="appHeader">
					<div id="appLogo">Logo</div>
					<nav id="appNav">
						<ul>
							<li>Nav Link 1</li>
							<li>Nav Link 2</li>
							<li>Nav Link 3</li>
						</ul>
					</nav>
					<div id="appLogin">Login</div>
				</header>
			);
		}
	})
})();