import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col justify-evenly items-center h-screen max-h-screen">
      <div id="head" className="flex flex-col gap-2">
        <h1 className="text-4xl tracking-wider font-bold">Flavor-Savor</h1>
        <p className="text-sm font-mono"> ={">"} Store or Explore </p>
      </div>
      <div id="menu-points" className="flex flex-col justify-center items-start gap-3 w-2/6">
        <div>
          <p className="font-mono text-left p-1 text-xl cursor-default">{"=>"} <Link href="/store" className="transition-all duration-300 ease-in-out rounded-xl hover:bg-indigo-700 p-1 px-2 focus:bg-indigo-700 focus:outline-none hover:shadow-lg focus:shadow-lg shadow-indigo-950">Store</Link></p>

          <p className="font-mono text-left p-1 text-xl cursor-default">{"=>"} <Link href="/explore" className="transition-all duration-300 ease-in-out rounded-xl hover:bg-indigo-700 p-1 px-2 focus:bg-indigo-700 focus:outline-none hover:shadow-lg focus:shadow-lg shadow-indigo-950">Explore</Link></p>
        </div>
      </div>
    </div>
  );
}
