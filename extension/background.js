chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.local.set({ trustshieldEnabled: true });
});
