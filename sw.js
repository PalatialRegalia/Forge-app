/* Forge Kinetic service worker.
 *
 * The app is three files and no build step, so this is deliberately small.
 * The strategy is chosen to make the worst failure mode - being stuck on a
 * stale index.html - impossible:
 *
 *   page loads (navigate)  network first, cache as a side effect
 *                          -> fresh whenever online, still opens offline
 *   everything else        cache first, network fallback
 *                          -> the icon and manifest never change mid-session
 *
 * Bump CACHE whenever you ship a change to index.html, manifest.json or
 * icon.svg, otherwise the old copy stays in the cache forever.
 */
const CACHE = 'forge-v1';
const SHELL = ['./', 'index.html', 'manifest.json', 'icon.svg'];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE)
      .then((cache) => cache.addAll(SHELL))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(
        keys.filter((key) => key !== CACHE).map((key) => caches.delete(key))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const request = event.request;
  if (request.method !== 'GET') return;
  if (new URL(request.url).origin !== self.location.origin) return;

  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then((response) => {
          const copy = response.clone();
          caches.open(CACHE).then((cache) => cache.put(request, copy));
          return response;
        })
        .catch(() => caches.match(request).then((hit) => hit || caches.match('index.html')))
    );
    return;
  }

  event.respondWith(
    caches.match(request).then((hit) => hit || fetch(request))
  );
});
