import financialStats from '$data/financialStats.json';

/** @type {import('./$types').PageServerLoad} */
export function load() {
	// In a real app, you might fetch this from an API
	// but for now we'll load it from our static JSON file.
	return {
		stats: financialStats
	};
}