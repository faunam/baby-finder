import { useEffect } from 'react';

const useScript = url => {
  useEffect(() => {
    const head = document.querySelector("head");
    const script = document.createElement('script');

    script.src = url;
    script.async = true;

    head.appendChild(script);

    return () => {
        head.body.removeChild(script);
    }
  }, [url]);
};

export default useScript;