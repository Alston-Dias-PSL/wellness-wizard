import React, { useEffect } from 'react';
export default function ChatBot (){
  useEffect(() => {
    window.watsonAssistantChatOptions = {
      integrationID: "27b1a797-5da8-4e4a-8fe2-f6e060c65597",
      region: "us-south",
      serviceInstanceID: "b9c7c642-a9d1-4526-acea-4f39d9aeec41",
      onLoad: async (instance) => { await instance.render(); }
    };
    const script = document.createElement('script');
    script.src = `https://web-chat.global.assistant.watson.appdomain.cloud/versions/${window.watsonAssistantChatOptions.clientVersion || 'latest'}/WatsonAssistantChatEntry.js`;
    document.head.appendChild(script);
    return () => {
      // Clean up: remove the script when the component is unmounted
      document.head.removeChild(script);
    };
  }, []); // Empty dependency array to run the effect only once on mount
  return (
    <div>
      {/* You can add any additional components or UI elements here */}
    </div>
  );
};