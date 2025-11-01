from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coffee & Empowerment</title>
    <script crossorigin src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
    <script crossorigin src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { margin: 0; padding: 0; }
    </style>
</head>
<body>
    <div id="root"></div>
    
    <script type="text/babel">
        const { useState, useEffect } = React;

        const Coffee = ({ size = 24, className = "" }) => (
            <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}>
                <path d="M17 8h1a4 4 0 1 1 0 8h-1"/>
                <path d="M3 8h14v9a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4Z"/>
                <line x1="6" x2="6" y1="2" y2="4"/>
                <line x1="10" x2="10" y1="2" y2="4"/>
                <line x1="14" x2="14" y1="2" y2="4"/>
            </svg>
        );

        const Sparkles = ({ size = 24, className = "" }) => (
            <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}>
                <path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z"/>
                <path d="M5 3v4"/>
                <path d="M19 17v4"/>
                <path d="M3 5h4"/>
                <path d="M17 19h4"/>
            </svg>
        );

        const Heart = ({ size = 24, className = "" }) => (
            <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}>
                <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>
            </svg>
        );

        const quotes = [
            {
                text: "She believed she could, so she did.",
                author: "R.S. Grey"
            },
            {
                text: "A strong woman looks a challenge in the eye and gives it a wink.",
                author: "Gina Carey"
            },
            {
                text: "The question isn't who's going to let me; it's who's going to stop me.",
                author: "Ayn Rand"
            },
            {
                text: "I am not free while any woman is unfree, even when her shackles are very different from my own.",
                author: "Audre Lorde"
            },
            {
                text: "There is no limit to what we, as women, can accomplish.",
                author: "Michelle Obama"
            },
            {
                text: "A woman is the full circle. Within her is the power to create, nurture and transform.",
                author: "Diane Mariechild"
            },
            {
                text: "Strong women don't have attitudes, they have standards.",
                author: "Unknown"
            },
            {
                text: "The most courageous act is still to think for yourself. Aloud.",
                author: "Coco Chanel"
            },
            {
                text: "You are more powerful than you know; you are beautiful just as you are.",
                author: "Melissa Etheridge"
            },
            {
                text: "Empowered women empower women.",
                author: "Unknown"
            }
        ];

        function CoffeeEmpowerment() {
            const [currentQuote, setCurrentQuote] = useState(0);
            const [fade, setFade] = useState(true);

            const nextQuote = () => {
                setFade(false);
                setTimeout(() => {
                    setCurrentQuote((prev) => (prev + 1) % quotes.length);
                    setFade(true);
                }, 300);
            };

            useEffect(() => {
                const interval = setInterval(nextQuote, 8000);
                return () => clearInterval(interval);
            }, []);

            return (
                <div className="min-h-screen bg-gradient-to-br from-amber-50 via-orange-50 to-yellow-50 flex flex-col items-center justify-center p-6 relative overflow-hidden">
                    <div className="absolute top-10 left-10 opacity-10">
                        <Coffee size={100} className="text-amber-800" />
                    </div>
                    <div className="absolute bottom-10 right-10 opacity-10">
                        <Coffee size={100} className="text-amber-800" />
                    </div>
                    <div className="absolute top-1/3 right-20 opacity-5">
                        <Coffee size={150} className="text-amber-900" />
                    </div>

                    <div className="max-w-3xl w-full bg-white/80 backdrop-blur-sm rounded-3xl shadow-2xl p-12 relative z-10 border-4 border-amber-200">
                        <div className="text-center mb-8">
                            <div className="flex items-center justify-center gap-3 mb-4">
                                <Coffee className="text-amber-700" size={40} />
                                <h1 className="text-5xl font-bold text-amber-900">
                                    Coffee & Courage
                                </h1>
                                <Coffee className="text-amber-700" size={40} />
                            </div>
                            <p className="text-amber-700 text-lg font-medium flex items-center justify-center gap-2">
                                <Sparkles size={20} />
                                Empowering Women, One Cup at a Time
                                <Sparkles size={20} />
                            </p>
                        </div>

                        <div className={`my-12 transition-opacity duration-300 ${fade ? 'opacity-100' : 'opacity-0'}`}>
                            <div className="bg-gradient-to-r from-amber-100 to-orange-100 rounded-2xl p-8 shadow-lg border-2 border-amber-300">
                                <p className="text-2xl text-amber-900 font-serif italic text-center mb-4 leading-relaxed">
                                    "{quotes[currentQuote].text}"
                                </p>
                                <p className="text-right text-amber-700 font-semibold text-lg">
                                    — {quotes[currentQuote].author}
                                </p>
                            </div>
                        </div>

                        <div className="flex justify-center">
                            <button
                                onClick={nextQuote}
                                className="bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-700 hover:to-orange-700 text-white font-bold py-4 px-8 rounded-full shadow-lg transform hover:scale-105 transition-all duration-200 flex items-center gap-2"
                            >
                                <Heart size={20} />
                                Get Another Dose of Inspiration
                                <Sparkles size={20} />
                            </button>
                        </div>

                        <div className="mt-12 text-center">
                            <p className="text-amber-800 font-medium text-lg">
                                Like a perfect cup of coffee, strong women are bold, 
                                empowering, and impossible to ignore.
                            </p>
                        </div>
                    </div>

                    <div className="mt-6 text-amber-700 text-sm">
                        Quote {currentQuote + 1} of {quotes.length}
                    </div>
                </div>
            );
        }

        const root = ReactDOM.createRoot(document.getElementById('root'));
        root.render(<CoffeeEmpowerment />);
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
