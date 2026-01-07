document.addEventListener('DOMContentLoaded', function () {
	const h2 = document.querySelector('h2');
	if (!h2) return;

	let centered = false;
	let original = {};

	function storeOriginal() {
		original = {
			position: h2.style.position || '',
			top: h2.style.top || '',
			left: h2.style.left || '',
			transform: h2.style.transform || '',
			transition: h2.style.transition || '',
			margin: h2.style.margin || ''
		};
	}

	h2.style.cursor = 'pointer';

	h2.addEventListener('click', function () {
		if (!centered) {
			const rect = h2.getBoundingClientRect();
			storeOriginal();

			// Fix the element at its current viewport position
			h2.style.position = 'fixed';
			h2.style.top = rect.top + 'px';
			h2.style.left = rect.left + 'px';
			h2.style.margin = '0';

			// Force reflow so the browser registers the fixed position
			h2.getBoundingClientRect();

			// Add class that moves it to center using CSS transitions
			h2.classList.add('to-center');
			centered = true;
		} else {
			// Remove centering class to animate back
			h2.classList.remove('to-center');

			// After transition ends, restore original inline styles
			const cleanup = function (ev) {
				// wait for transform/left/top transition to finish
				h2.removeEventListener('transitionend', cleanup);
				h2.style.position = original.position;
				h2.style.top = original.top;
				h2.style.left = original.left;
				h2.style.transform = original.transform;
				h2.style.transition = original.transition;
				h2.style.margin = original.margin;
			};

			h2.addEventListener('transitionend', cleanup);
			centered = false;
		}
	});
});
