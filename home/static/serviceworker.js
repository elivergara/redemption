const CACHE_NAME = 'eg-app-cache-v1';
const urlsToCache = [
  '/', // Cache the homepage
  '/static/style.css', // Path to your CSS file
  '/static/js/main.js', // Placeholder for future JS file
  '/static/icons/icon-192x192.png', // Path to your app icon
  '/static/icons/icon-512x512.png'  // Path to your app icon
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(urlsToCache).catch((error) => {
        console.warn('Some assets failed to cache:', error);
      });
    })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
