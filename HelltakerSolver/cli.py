import click
import HelltakerSolver

@click.command()
@click.argument("mode", type=click.Choice(["BruteForce"]))
@click.argument("file", type=click.Path())
def run(mode, file):
    if mode == "BruteForce":
        click.echo("Solving... (this may take a while)")
        results = HelltakerSolver.load_bruteforce(file)
        click.echo("Results:")
        if not results:
            click.echo("None")
            return
        """ CURRENTLY BROKEN
            ## Awaiting click 8.0.2 for the fix
        
        def yield_out():
            for gp in results:
                yield f"\tRemaining Willpower: {gp.remaining_actions()}\n\t\tActions: {', '.join([action.lower() for action in gp.actions])}"
        click.echo_via_pager(yield_out)
        """
        for gp in results:
            click.echo(f"  Remaining Willpower: {gp.remaining_actions()}\n    Actions: {', '.join([action.lower() for action in gp.actions])}")