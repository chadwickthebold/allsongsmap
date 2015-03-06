//Application namespace
var asm = asm || {};

(function() {
	'use strict';

	var AppHeader = asm.Header,
			AppFooter = asm.Footer;

	asm.App = React.createClass({
		render: function() {
			return (
				<div>
					<AppHeader/>
					<section>Page Content</section>
				</div>
			)
		}
	});

	React.render(
		<asm.App/>, 
		document.getElementById('asm')
	);
})();