export default async function Explore() {
    type Recipe = {
        id: number;
        name: string;
        ingredients: string[];
        instructions: string;
    }


    async function fetchRecipes(): Promise<Recipe[]> {
        const response = await fetch("http://localhost:5000/api/v1/recipes");
        const recipes: Recipe[] = await response.json();
        return recipes;
    }

    async function renderRecipes() {
        const recipes = await fetchRecipes();

        const recipeList: JSX.Element[] = [];

        recipes.forEach((recipe) => {
            recipeList.push(<div className="flex relative flex-grow flex-col gap-1 overflow-hidden rounded-lg p-4 transition-all duration-300 ease-in-out shadow-md shadow-indigo-900 group" key={recipe.id}>
                <h2 className="font-bold tracking-wide text-lg">{recipe.name}</h2>
                <p className="italic">{recipe.ingredients.join(", ")}</p>
                <p>{recipe.instructions}</p>
                <span className="absolute transition-all ease-in-out duration-300 border-t-2 border-indigo-500 left-0 top-0 bottom-0 right-0 rounded-lg"></span>
                <span className="absolute transition-all ease-in-out duration-300 border-b-2 border-indigo-500 bottom-0 top-0 w-[0%] group-hover:w-full self-center group-hover:rounded-lg"></span>
                <span className="absolute transition-all ease-in-out duration-300 border-l-2 h-[0%] border-indigo-500 left-0 top-0 group-hover:h-full group-hover:rounded-lg right-0"></span>
                <span className="absolute transition-all ease-in-out duration-300 border-r-2 h-[0%] border-indigo-500 left-0 top-0 right-0 group-hover:h-full group-hover:rounded-lg"></span>
            </div>);
        });

        return recipeList;
    }

    await renderRecipes();

    return (
        <div className="flex flex-col justify-evenly items-center h-screen max-h-screen p-5">
        <div id="head" className="flex flex-col gap-2">
            <h1 className="text-4xl tracking-wider text-center font-bold">Explore Your Recipes</h1>
        </div>
        <div id="recipe-data" className="flex flex-row flex-wrap gap-3 justify-center items-center">
            {await renderRecipes()}
        </div>
        </div>
    );
}